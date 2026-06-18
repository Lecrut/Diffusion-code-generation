import json
import sys
def process_stream():
    for line in sys.stdin:
        try:
            data = json.loads(line)
            print(json.dumps(data))
        except json.JSONDecodeError as e:
            continue
if __name__ == '__main__':
    pass