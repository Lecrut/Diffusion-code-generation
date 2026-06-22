def convert_volumes(volume_file_path):
    try:
        with open(volume_file_path, 'r') as file:
            volumes = [float(line.strip()) for line in file]
        
        for volume in volumes:
            liters = volume
            cubic_meters = volume / 1000.0
            print(f"{liters} liters is equivalent to {cubic_meters:.3f} cubic meters")
    
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Error converting values in the file.")

if __name__ == '__main__':
    sample_volumes = """
1000
500
250
750
"""
    with open('sample_volumes.txt', 'w') as f:
        f.write(sample_volumes)
    
    convert_volumes('sample_volumes.txt')