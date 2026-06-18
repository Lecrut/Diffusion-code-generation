def gen(threshold):
          n = 0
          while True:
              if n > threshold:
                  yield True   # Only happens ONCE since we'll handle subsequent differently or just keep yielding based on same rule? 
                              # Wait wording says "yields True ONLY WHEN the first number ...". Implies exclusivity.

if __name__ == '__main__':
    pass
