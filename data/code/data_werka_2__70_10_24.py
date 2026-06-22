from collections import namedtuple

def fetch_edge_entries(sequence):
    if not sequence:
        raise ValueError("Sequence must contain at least one element")
    result = namedtuple("EdgeEntry", "first last")
    if len(sequence) == 1:
        return result(sequence[0], sequence[0])
    return result(sequence[0], sequence[-1])

if __name__ == '__main__':
    words = ["start", "middle", "end"]
    edges = fetch_edge_entries(words)
    print(edges.first)
    print(edges.last)