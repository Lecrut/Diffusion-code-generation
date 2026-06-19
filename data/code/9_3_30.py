def convert_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes = file.readlines()
        
        for volume in volumes:
            volume = float(volume.strip())
            liters = volume
            cubic_meters = volume / 1000
            print(f"{liters} liters is equivalent to {cubic_meters} cubic meters")
    
    except FileNotFoundError:
        print("Error: The file was not found.")
    except ValueError:
        print("Error: The file contains non-numeric data.")

if __name__ == '__main__':
    sample_volumes = [1000, 2000, 500]
    with open('sample_volumes.txt', 'w') as f:
        for volume in sample_volumes:
            f.write(f"{volume}\n")
    
    convert_volumes('sample_volumes.txt')