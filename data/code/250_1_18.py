import numpy as np

def calculate_average(data):
    return np.mean(data)

if __name__ == '__main__':
    sample_data = {
        'list1': [1.0, 2.0, 3.0, 4.0, 5.0],
        'list2': [10.5, 20.5, 30.5]
    }
    
    for key, data in sample_data.items():
        avg = calculate_average(data)
        print(f"Average of {key}: {avg}")