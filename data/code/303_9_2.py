import asyncio
import time
async def fetch_timestamp(delay):
    await asyncio.sleep(delay)
    return time.time()
async def calculate_elapsed_time(delay1, delay2):
    start_time = time.time()
    await asyncio.gather(
        fetch_timestamp(delay1),
        fetch_timestamp(delay2)
    )
    end_time = time.time()
    return end_time - start_time
async def main():
    delay_a = 0.5
    delay_b = 1.0
    print("Calculating elapsed time between two remote calls...")
    elapsed = await calculate_elapsed_time(delay_a, delay_b)
    print(f"Elapsed time: {elapsed:.4f} seconds")
if __name__ == '__main__':
    asyncio.run(main())