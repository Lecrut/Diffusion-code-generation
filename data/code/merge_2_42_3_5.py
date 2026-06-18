import sys
def sort_mixed_data(data):
    converted = [str(item) for item in data]
    return ",".join(sorted(converted))
if __name__ == '__main__':
    sample_values = ["banana", 3, "apple", 10, "cherry"]
    result = sort_mixed_data(sample_values)
    print(result)