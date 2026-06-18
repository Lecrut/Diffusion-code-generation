import sys; print(lambda s: ''.join(reversed(s))(sys.argv[1] if len(sys.argv) > 1 else "Hello World")) # This will fail on execution due to argv requirement, let's fix it per constraints: import string; def rev(s): return "".join(reversed(str(s))); [print(f"Input: {s}, Output: {rev(s)}") for s in ["abc", "!@#"]]

if __name__ == '__main__':
    pass
