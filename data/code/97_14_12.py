def truth_table_or():
    return [{'A': True, 'B': True, 'A or B': True}, {'A': True, 'B': False, 'A or B': True}, {'A': False, 'B': True, 'A or B': True}, {'A': False, 'B': False, 'A or B': False}]

if __name__ == '__main__':
    print(truth_table_or())