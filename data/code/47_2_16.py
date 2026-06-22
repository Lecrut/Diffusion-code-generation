import numpy as np

def calculate_mean(data):
    try:
        array_data = np.array(data)
        if array_data.size == 0:
            raise ValueError("Input dataset cannot be empty.")
        if not np.issubdtype(array_data.dtype, np.number):
            raise TypeError("All elements in the dataset must be numeric.")
        result = np.mean(array_data)
        return result
    except Exception as e:
        raise type(e)(f"Failed to calculate mean: {str(e)}")

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    computed_mean = calculate_mean(sample_values)
    print(computed_mean)