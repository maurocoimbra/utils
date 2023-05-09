import os
import librosa
import soundfile as sf

TARGET_SAMPLING_RATE = 24000

def execute_conversion(input_filepath, output_filepath, target_sr):

    waveform, sr = librosa.load(input_filepath, sr=None)
    target_waveform = librosa.resample(waveform, orig_sr=sr, target_sr=target_sr)
    sf.write(output_filepath, target_waveform, target_sr, format='wav')


for genre in os.listdir('files'):
    for file_name in os.listdir(f'files/{genre}'):
        new_file_name = file_name.split('.')[0] + '.wav'

        output_folder = (f'converted_files/{genre}')

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        execute_conversion(f'files/{genre}/{file_name}', f'{output_folder}/{new_file_name}', TARGET_SAMPLING_RATE)
        print(f'Sucessfully converted audio file {file_name} to {output_folder}/{new_file_name}')