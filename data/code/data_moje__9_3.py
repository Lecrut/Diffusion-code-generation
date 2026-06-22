import csv
import io

def convert_volumes(volumes_liters):
    results = []
    for vol in volumes_liters:
        cubic_meters = vol / 1000.0
        results.append((vol, cubic_meters))
    return results

def read_and_convert(file_path):
    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.reader(f)
            volumes = []
            for row in reader:
                if not row:
                    continue
                try:
                    val = float(row[0])
                    volumes.append(val)
                except ValueError:
                    continue
            return convert_volumes(volumes)
    except FileNotFoundError:
        return []
    except PermissionError:
        return []

def main():
    content = "1000\n2000\n500\n"
    file_path = "volumes.csv"
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    results = read_and_convert(file_path)
    
    for liters, cubic_meters in results:
        print(f"{liters} liters is {cubic_meters} cubic meters")

if __name__ == '__main__':
    main()