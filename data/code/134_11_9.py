def are_tuples_disjoint(tuple1, tuple2, tuple3):
    set1 = set(tuple1)
    set2 = set(tuple2)
    set3 = set(tuple3)
    
    if not (isinstance(set1, set) and isinstance(set2, set) and isinstance(set3, set)):
        raise ValueError("All inputs must be tuples.")
    
    return set1.isdisjoint(set2) and set2.isdisjoint(set3) and set1.isdisjoint(set3)

if __name__ == '__main__':
    tuple1 = (1, 2)
    tuple2 = (3, 4)
    tuple3 = (5, 6)
    
    print(f"Tuples: {tuple1}, {tuple2}, {tuple3}")
    print(f"Disjoint: {are_tuples_disjoint(tuple1, tuple2, tuple3)}")