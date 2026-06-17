def check_descending(strings):
    results = []
    for i in range(len(strings) - 1):
        current = strings[i]
        next_str = strings[i+1]
        if current > next_str:
            results.append(True)
        else:
            results.append(False)
    return results
if __name__ == '__main__':
    sample_list = ["apple", "banana", "date", "cherry", "fig"]
    output = check_descending(sample_list)
    print(output)