import numpy as np

def calculate_mean(data):
    return np.mean(data)

if __name__ == '__main__':
    data1 = [10, 20, 30, 40, 50]
    data2 = [5, 15, 25]
    data3 = []
    data4 = [7.5, 8.5, 9.5]
    
    print(f"Mean of {data1}: {calculate_mean(data1)}")
    print(f"Mean of {data2}: {calculate_mean(data2)}")
    print(f"Mean of {data3}: {calculate_mean(data3)}")
    print(f"Mean of {data4}: {calculate_mean(data4)}")