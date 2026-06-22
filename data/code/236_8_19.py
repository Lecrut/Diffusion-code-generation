def repeat_shape():
    shape = "O\n"
    repeated_shape = (shape * 20).rstrip()
    return repeated_shape

if __name__ == '__main__':
    print(repeat_shape())