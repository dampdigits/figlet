# Pyfiglet
import sys
import random
from pyfiglet import Figlet

argc = len(sys.argv)
# Check for improper usage
if argc == 2 or argc > 3:
    print("Invalid usage")
    sys.exit(-1)

figlet = Figlet()
# Store list of Figlet fonts
fonts = list(figlet.getFonts())

# Select random font if not specified
if argc == 1:
    random_font = random.choice(fonts)
    figlet.setFont(font=random_font)

else:
    # Check for improper usage
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        print(" Invalid Usage")
        sys.exit(1)
    # Set to specified font if valid
    if sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
    else:
        print("Invalid Usage")
        sys.exit(2)

# Input text
text = input("Input: ")
# Display figlet
print("\n", figlet.renderText(text), "\n")

sys.exit(0)
