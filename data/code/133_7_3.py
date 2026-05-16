def stringlist_to_boollist(stringlist):
    boollist = []
    for s in stringlist:
        if s == 'True':
            boollist.append(True)
        elif s == 'False':
            boollist.append(False)
        else:
            raise ValueError("Invalid string encountered")
    return boollist
if __name__ == '__main__':
    sample_list = ['True', 'False', 'True', 'False']
    result = stringlist_to_boollist(sample_list)
    print(result)