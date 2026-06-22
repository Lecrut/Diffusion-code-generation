def calculate_mean(data):
    return sum(data) / len(data) if data else 0

if __name__ == '__main__':
    datasets = [
        [1, 2],
        [3, 4, 5],
        [6]
    ]
    
    for dataset in datasets:
        print(f"Mean of {dataset}: {calculate_mean(dataset)}")