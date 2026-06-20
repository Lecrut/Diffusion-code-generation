def truth_table_or():
    return [{'A': True, 'B': True, 'OR': True}, {'A': True, 'B': False, 'OR': True}, {'A': False, 'B': True, 'OR': True}, {'A': False, 'B': False, 'OR': False}]

if __name__ == '__main__':
    print(truth_table_or())