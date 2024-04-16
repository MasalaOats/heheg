# Import the Pyrogram client from auth.py
from auth import app

# Import all command handlers and message handlers from handlers.py
import handlers

# Optional: Import additional configurations or utility functions if needed
# from config import ...
# from utils import ...

# Main function to run the bot
def main():
    # Start the Pyrogram client and run the bot
    app.run()

# Entry point of the script
if __name__ == "__main__":
    main()
