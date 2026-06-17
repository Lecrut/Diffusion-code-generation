import asyncio
import time
async def fetch_timestamp(delay):
    await asyncio.sleep(delay)
    return time.time()
async def calculate_elapsed_time(delay1, delay2):
    start_time = time.time()
    t1 = await fetch_timestamp(delay1)
    t2 = await fetch_timestamp(delay2)
    end_time = time.time()
    return end_time - start_time
async def main():
    delay_a = 1.5
    delay_b = 0.5
    print(f"Calculating elapsed time for delays: {delay_a}s and {delay_b}s")
    elapsed = await calculate_elapsed_time(delay_a, delay_b)
    print(f"Elapsed time calculated: {elapsed:.4f} seconds")
if __name__ == '__main__':
    asyncio.run(main())