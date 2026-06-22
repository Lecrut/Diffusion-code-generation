import sys

class VolumeConverter:
    def __init__(self, volume_list):
        self.volume_list = volume_list

    def convert(self):
        results = []
        for value in self.volume_list:
            try:
                number = float(value)
                liters = number
                cubic_meters = number / 1000
                results.append((liters, cubic_meters))
            except ValueError:
                results.append(None)
        return results

def process_volumes_from_string(data):
    try:
        lines = data.strip().split('\n')
        volume_list = []
        for line in lines:
            line = line.strip()
            if line:
                volume_list.append(line)
        
        converter = VolumeConverter(volume_list)
        return converter.convert()
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    sample_data = "100\n500\n2500\ninvalid\n0.5"
    output = process_volumes_from_string(sample_data)
    for item in output:
        if item is None:
            print("Error parsing input")
        else:
            print(f"Liters: {item[0]}, Cubic Meters: {item[1]}")