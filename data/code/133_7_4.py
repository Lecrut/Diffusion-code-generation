def stringlist_to_boollist(stringlist):
    boollist = []
    for s in stringlist:
        if s == 'True':
            boollist.append(True)
        elif s == 'False':
            boollist.append(False)
        else:
            raise ValueError(f"Unexpected string encountered: {s}")
    return boollist
if __name__ == '__main__':
    sample_input = ['True', 'False', 'True', 'False']
    result = stringlist_to_boollist(sample_input)
    print(result)