def convert_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes = file.readlines()
        for volume in volumes:
            volume = float(volume.strip())
            liters = volume
            cubic_meters = volume / 1000
            print(f'Liters: {liters}, Cubic Meters: {cubic_meters}')
    except FileNotFoundError:
        print('File not found.')
    except ValueError:
        print('Invalid volume value.')
if __name__ == '__main__':
    sample_volumes = '1000\n2000\n3000'
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+t')
    temp_file.write(sample_volumes)
    temp_file.close()
    convert_volumes(temp_file.name)
    import os
    os.unlink(temp_file.name)