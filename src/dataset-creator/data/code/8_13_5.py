import asyncio
from collections import deque
class StreamProcessor:
    def __init__(self):
        self.buffer = deque()
        self.max_buffer_size = 1024 * 1024
        self.processed_count = 0
    async def process_stream(self, data_generator):
        while True:
            try:
                item = await asyncio.get_event_loop().run_in_executor(None, lambda: next(data_generator))
                if isinstance(item, (int, float)):
                    threshold_check = item > 50
                    if threshold_check and self.processed_count < 10:
                        action_triggered(self)
            except StopAsyncIteration:
                break
    def action_triggered(self):
        print(f"Action triggered. Processed count: {self.processed_count}")
async def generate_sample_data():
    for i in range(25):
        yield float(i * 10 + random.random())
import random
if __name__ == '__main__':
    processor = StreamProcessor()
    async def main():
        data_gen = generate_sample_data()
        await asyncio.get_event_loop().run_in_executor(None, lambda: next(data_gen))
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    except Exception as e:
        print(f"Error occurred: {e}")