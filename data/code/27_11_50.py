def values_differ(a, b):
    return a != b

if __name__ == '__main__':
    sample1 = [1, 2, 3]
    sample2 = (1, 2, 3)
    print(values_differ(sample1, sample2))
    
    sample3 = {'key': 'value'}
    sample4 = {'key': 'value'}
    print(values_differ(sample3, sample4))
    
    sample5 = 10.0
    sample6 = 10
    print(values_differ(sample5, sample6))
    
    sample7 = "same_string"
    sample8 = "same_string"
    print(values_differ(sample7, sample8))
    
    sample9 = None
    sample10 = False
    print(values_differ(sample9, sample10))