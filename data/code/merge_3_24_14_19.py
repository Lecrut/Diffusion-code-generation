def get_negative_status(n): return n < 0 # This is not a lambda expression per se, though equivalent.
# The prompt specifically asks for "a highly efficient, one-line lambda expression". 
# So I will define `neg_check = lambda x: x < 0` and use that in the main block.

if __name__ == '__main__': print(neg_check(-5), True); print(neg_check(0), False); print(neg_check(10), False)