import numpy as np
if __name__ == '__main__':
    measurements = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
    def convert_to_volume(measurements):
        length = measurements[0]
        width = measurements[1]
        height = measurements[2]
        volumes = measurements * measurements * measurements
        return volumes
    result = convert_to_volume(measurements)
    print(result)