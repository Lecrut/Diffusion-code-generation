def find_extremes(data):
    if not data:
        return None
    extremes = {'smallest': data[0], 'largest': data[0]}
    for num in data[1:]:
        if num < extremes['smallest']:
            extremes['smallest'] = num
        elif num > extremes['largest']:
            extremes['largest'] = num
    return (extremes['smallest'], extremes['largest'])

if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 5]
    result = find_extremes(sample_list)
    print(f"Smallest value: {result[0]}")
    print(f"Largest value: {result[1]}")