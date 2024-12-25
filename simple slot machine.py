import random

def spin_slot_machine():
    symbols = ['🍒', '🍋', '🍊', '🍉', '🍇', '💰']
    
    # Randomly select three symbols to represent the slots
    return [random.choice(symbols) for _ in range(3)]

def check_win(spins):
    # Check if all three symbols are the same
    return spins[0] == spins[1] == spins[2]

def main():
    print(" Welcome to the Simple Slot Machine! ")
    
    while True:
        input(" Press Enter to spin the slots... ")
        
        spins = spin_slot_machine()
        print("Spinning... ", spins)
        
 
        if check_win(spins):
            print("Congratulations! You won!")
        else:
            print("Sorry, you lost. Better luck next time!")
        
    
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
