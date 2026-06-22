TRUE_VALUE = True
FALSE_VALUE = False

def toggle_bools(stream):
    for element in stream:
        if element is TRUE_VALUE:
            yield FALSE_VALUE
        elif element is FALSE_VALUE:
            yield TRUE_VALUE
        else:
            raise ValueError("Non-boolean item encountered")

def execute():
    source = [True, True, False, True, False]
    toggled = list(toggle_bools(source))
    print(toggled)

if __name__ == '__main__':
    execute()