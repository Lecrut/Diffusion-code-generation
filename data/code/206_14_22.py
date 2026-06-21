min_value = lambda lst: min(lst) if lst else None

if __name__ == '__main__':
    data_points = [
        [3, 1, 4, 1, 5],
        [7],
        []
    ]
    
    for dp in data_points:
        print(f"Minimum in {dp}: {min_value(dp)}")