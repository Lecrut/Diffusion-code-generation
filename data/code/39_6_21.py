def find_all_occurrences(text, pattern):

    def helper_find_next(start_index):
        index = text.find(pattern, start_index)
        if index == -1:
            return None
        return (index, index + len(pattern))
    occurrences = []
    index = 0
    while True:
        next_occurrence = helper_find_next(index)
        if next_occurrence is None:
            break
        occurrences.append(next_occurrence)
        index = next_occurrence[1]
    return occurrences
if __name__ == '__main__':
    text_sample = 'banana'
    pattern_sample = 'ana'
    result = find_all_occurrences(text_sample, pattern_sample)
    print(result)
    text_sample_2 = 'mississippi'
    pattern_sample_2 = 'issi'
    result_2 = find_all_occurrences(text_sample_2, pattern_sample_2)
    print(result_2)