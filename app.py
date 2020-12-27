# Foreground: '\033[..m'
foreground_start = 30
foreground_end = 37

# Background: '\033[..m'
background_start = 40
background_end = 47

# Opening: '\033['
opening = "\033["

# Closing: '\033[0m'
closing = "\033[0m"


def main():
	print("Kip's Terminal Colors!")
	print("------------------------------------------------")
	print("| Bg | Foreground                              |")
	print("------------------------------------------------")
	
	for back in range(background_start, background_end+1):
		print(f"| {back} | {opening}{back}m", end="")
		for front in range(foreground_start, foreground_end+1):
			print(f"{opening}{front}m{front}   ", end="")

		print(f"{closing}|")
		print(f"| {back} | {opening}{back}m", end="")

		for front in range(foreground_start, foreground_end+1):
			print(f"{opening}1;{front}m1;{front} ", end="")

		print(f"{closing}|")
		print("------------------------------------------------")


if __name__ == "__main__":
	main()