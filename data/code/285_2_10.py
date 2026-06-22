def compare_consecutive_elements(tup):
    return {tup[i:i+2]: tup[i] < tup[i+1] for i in range(len(tup) - 1)}

if __name__ == '__main__':
    sample_tuple = (3, 5, 2, 8, 1)
    print(compare_consecutive_elements(sample_tuple))