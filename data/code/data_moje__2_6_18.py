import numpy as np

def scale_volumes(volumes, scaling_factors):
    volumes_array = np.asarray(volumes, dtype=np.float64)
    factors_array = np.asarray(scaling_factors, dtype=np.float64)
    scaled_volumes = volumes_array * factors_array
    total_volume = np.sum(scaled_volumes)
    mean_volume = np.mean(scaled_volumes)
    return scaled_volumes, total_volume, mean_volume

if __name__ == '__main__':
    sample_volumes = [10.5, 20.3, 15.7, 30.0, 5.2]
    sample_factors = [1.2, 0.8, 1.5, 2.0, 0.5]
    result_scaled, result_total, result_mean = scale_volumes(sample_volumes, sample_factors)
    print(result_scaled)
    print(result_total)
    print(result_mean)