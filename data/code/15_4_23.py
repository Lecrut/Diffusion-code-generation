def matching_pairs(value1, value2, pairs_list):
    for pair in pairs_list:
        if pair[0] == value1 and pair[1] == value2:
            yield True
        else:
            yield False

if __name__ == '__main__':
    sample_value1 = 'apple'
    sample_value2 = 'banana'
    sample_pairs_list = [
        ('apple', 'banana'),
        ('orange', 'grape'),
        ('apple', 'orange'),
        ('banana', 'apple')
    ]
    
    for result in matching_pairs(sample_value1, sample_value2, sample_pairs_list):
        print(result)