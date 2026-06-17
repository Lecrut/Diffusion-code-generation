import math
def determine_most_weight_efficient_storage(measurements):
    if not measurements:
        return None, 0.0
    n = len(measurements)
    if n == 1:
        return measurements[0], 0.0
    weights = [math.sqrt(m**2) for m in measurements]                                                                                                                                                                
    if n > 1:
        mean = sum(measurements) / n
        centered_data = [m - mean for m in measurements]
        scatter_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                scatter_matrix[i][j] = centered_data[i] * centered_data[j]
        try:
            eigenvalues, eigenvectors = np.linalg.eigh(scatter_matrix)
        except ImportError:
            raise RuntimeError("NumPy is required for efficient eigenvalue decomposition.")
        sorted_indices = np.argsort(eigenvalues)[::-1]
        most_efficient_direction_index = sorted_indices[0]
        projection = [np.dot(centered_data[i], eigenvectors[:, most_efficient_direction_index]) for i in range(n)]
        return projection, eigenvalues[most_efficient_direction_index]
    return None, 0.0
if __name__ == '__main__':
    import numpy as np
    sample_measurements = [
        1.0, 2.0, 3.0, 4.0, 5.0,                                           
        1.1, 2.1, 3.1, 4.1, 5.1                                                                          
    ]
    print(f"Original Measurements: {sample_measurements}")
    try:
        result_projection, efficiency_score = determine_most_weight_efficient_storage(sample_measurements)
        if result_projection is not None:
            print("\n--- Weight-Efficient Storage Result (Projection onto PC1) ---")
            print(f"Most Efficient Stored Unit (Projection): {result_projection}")
            print(f"Efficiency Score (Variance captured by this dimension): {efficiency_score:.4f}")
        else:
            print("Could not determine efficient storage.")
    except RuntimeError as e:
        print(f"\nError during execution: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")