FIRST_ITEM_INDEX = 0
LAST_ITEM_INDEX = -1

def check_sequence(seq):
    return (seq[FIRST_ITEM_INDEX], seq[LAST_ITEM_INDEX]) if seq else (None, None)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30)
    empty_list = []
    empty_tuple = ()
    print(check_sequence(sample_list))
    print(check_sequence(sample_tuple))
    print(check_sequence(empty_list))
    print(check_sequence(empty_tuple))