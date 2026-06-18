def sort_and_join(data):
    converted = [str(item) for item in data]
    return ",".join(sorted(converted))
if __name__ == '__main__':
    sample_data = ["banana", 3, "apple", 10, "cherry"]
    result = sort_and_join(sample_data)
    print(result)