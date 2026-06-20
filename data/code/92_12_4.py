def opposite_truth(value):
    return 'True' if value.lower() == 'false' else 'False'
if __name__ == '__main__':
    print(opposite_truth('True'))
    print(opposite_truth('FALSE'))
    print(opposite_truth('true'))
    print(opposite_truth('fAlSe'))