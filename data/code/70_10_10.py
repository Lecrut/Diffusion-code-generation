def extract_boundary_elements(source):
    if len(source) < 1:
        raise ValueError("Source list must contain at least one element")
    if len(source) == 1:
        return (source[0], source[0])
    return (source[0], source[-1])

if __name__ == '__main__':
    items = ["red", "green", "blue", "yellow"]
    first, last = extract_boundary_elements(items)
    print(first)
    print(last)