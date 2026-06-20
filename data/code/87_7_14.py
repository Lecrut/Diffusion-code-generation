class BooleanCombiner:
    def combine(self, expr1, expr2):
        return (expr1 and not expr2) or (not expr1 and expr2)

if __name__ == '__main__':
    combiner = BooleanCombiner()
    
    sample_expr1 = True
    sample_expr2 = False
    result = combiner.combine(sample_expr1, sample_expr2)
    print(result)
    
    sample_expr1 = False
    sample_expr2 = True
    result = combiner.combine(sample_expr1, sample_expr2)
    print(result)
    
    sample_expr1 = True
    sample_expr2 = True
    result = combiner.combine(sample_expr1, sample_expr2)
    print(result)
    
    sample_expr1 = False
    sample_expr2 = False
    result = combiner.combine(sample_expr1, sample_expr2)
    print(result)