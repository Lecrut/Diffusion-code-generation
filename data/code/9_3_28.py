def convert_volumes(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes_ml = [float(line.strip()) for line in file if line.strip()]
        
        volumes_l = [v / 1000 for v in volumes_ml]
        volumes_m3 = [v / 1_000_000 for v in volumes_ml]
        
        return volumes_l, volumes_m3
    except FileNotFoundError:
        print("File not found.")
        return [], []
    except ValueError:
        print("Invalid data in file.")
        return [], []

if __name__ == '__main__':
    sample_data = """1000
2000
500"""
    
    with open('sample_volumes.txt', 'w') as f:
        f.write(sample_data)
    
    liters, cubic_meters = convert_volumes('sample_volumes.txt')
    
    print("Volumes in liters:", liters)
    print("Volumes in cubic meters:", cubic_meters)