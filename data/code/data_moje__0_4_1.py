def read_lengths_from_file(filename):
    with open(filename, 'r') as f:
        return [float(line.strip()) for line in f if line.strip()]

def meters_to_yards(meters):
    return meters * 1.09361

def convert_lengths(meters_list):
    return [meters_to_yards(m) for m in meters_list]

def main():
    import tempfile
    import os

    sample_meters = [10, 100, 0.5, 1000]
    
    fd, path = tempfile.mkstemp(suffix='.txt')
    try:
        with os.fdopen(fd, 'w') as f:
            for m in sample_meters:
                f.write(f"{m}\n")
        
        meters_list = read_lengths_from_file(path)
        yards_list = convert_lengths(meters_list)
        
        for m, y in zip(meters_list, yards_list):
            print(f"{m} meters is {y} yards")
    finally:
        os.close(fd)
        os.unlink(path)

if __name__ == '__main__':
    main()