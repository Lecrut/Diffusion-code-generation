import random

def calculate_median(data):
    data.sort()
    n = len(data)
    if n % 2 == 0:
        return (data[n//2 - 1] + data[n//2]) / 2
    else:
        return data[n//2]

if __name__ == '__main__':
    sample_data = [random.randint(1, 1000) for _ in range(100)]
    print(calculate_median(sample_data))