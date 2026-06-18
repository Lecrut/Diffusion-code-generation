data = {"a": 50, "b": -10, "c": 25}
filtered_data = {k: v for k, v in data.items() if v > 0}
sorted_data = dict(sorted(filtered_data.items()))
if __name__ == '__main__':
    print("Filtered and Sorted Data:", sorted_data)