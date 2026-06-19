def convert_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    converted_volumes = []
    for volume in volumes:
        try:
            cubic_meters = float(volume.strip())
            liters = cubic_meters * 1000
            converted_volumes.append((cubic_meters, liters))
        except ValueError:
            print(f"Invalid value: {volume.strip()}")

    return converted_volumes

if __name__ == '__main__':
    sample_data = """0.5\n1.2\n3.7\n"""
    with open('sample_volumes.txt', 'w') as file:
        file.write(sample_data)

    result = convert_volumes('sample_volumes.txt')
    for cm, l in result:
        print(f"{cm} cubic meters is equivalent to {l} liters")