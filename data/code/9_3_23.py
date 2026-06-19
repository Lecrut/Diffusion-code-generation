def convert_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes = file.readlines()
        for volume in volumes:
            try:
                cubic_meters = float(volume.strip())
                liters = cubic_meters * 1000
                print(f'{cubic_meters} m³ is equivalent to {liters} L')
            except ValueError:
                print(f'Invalid volume value: {volume.strip()}')
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print(f'An error occurred: {e}')
if __name__ == '__main__':
    sample_data = '0.5\n1.2\n3.4\ninvalid\n2.0'
    with open('sample_volumes.txt', 'w') as file:
        file.write(sample_data)
    convert_volumes('sample_volumes.txt')