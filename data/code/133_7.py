def stringlist_to_boollist(stringlist):
    result = []
    for s in stringlist:
        if s == 'True':
            result.append(True)
        elif s == 'False':
            result.append(False)
        else:
            raise ValueError("Invalid string encountered")
    return result
if __name__ == '__main__':
    sample_list = ['True', 'False', 'True', 'False']
    boolean_list = stringlist_to_boollist(sample_list)
    print(boolean_list)