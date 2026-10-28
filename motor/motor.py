"""Simulate motor commands without connecting to physical hardware."""


def move(speed):
    print(f"  Motor: move forward at {speed:.1f} m/s")

def stop():
    print("  Motor: STOP")


if __name__ == "__main__":
<<<<<<< HEAD
    move(11.0)
=======
    move(14.0)
>>>>>>> motor-dev
    stop()
