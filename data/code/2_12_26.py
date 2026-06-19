class VolumeScaler:
    def __init__(self, initial_data):
        self.data = list(initial_data)
    
    def scale(self, factor):
        return [x * factor for x in self.data]

if __name__ == '__main__':
    sample_data = [1.0, 2.5, 3.75, 4.2]
    scaler = VolumeScaler(sample_data)
    scaling_factor = 2
    scaled_data = scaler.scale(scaling_factor)
    print(scaled_data)