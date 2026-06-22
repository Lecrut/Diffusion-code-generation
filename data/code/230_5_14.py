LENGTH_SET = set()

def unique_lengths(string_set):
    global LENGTH_SET
    LENGTH_SET.update({len(s) for s in string_set})
    return sorted(LENGTH_SET)

if __name__ == '__main__':
    sample_set = {"apple", "banana", "cherry", "date"}
    print(unique_lengths(sample_set))