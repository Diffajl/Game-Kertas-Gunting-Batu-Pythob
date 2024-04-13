import random

def game():
    print("""
+-----------------------------------------------+
|   Selamat Datang Di Game Kertas Gunting Batu  |
+-----------------------------------------------+
""")
    
    while True:
        computer_choice = random.choice(["kertas", "gunting", "batu"])

        user_choice = input("( Kertas / Gunting / Batu ) : ").lower()

        if user_choice == computer_choice:
            print(f"Game Seri!. Kamu memilih {user_choice} dan komputer memilih {computer_choice}")
            print("\t")

        elif (
            (user_choice == "kertas" and computer_choice == "batu") or 
            (user_choice == "gunting" and computer_choice == "kertas") or
            (user_choice == "batu" and computer_choice == "gunting")
        ):
            print(f"Kamu Menang!. Kamu memilih {user_choice} dan komputer memilih {computer_choice}")
            print("\t")

        elif (
            (user_choice == "kertas" and computer_choice == "gunting") or
            (user_choice == "gunting" and computer_choice == "batu") or
            (user_choice == "batu" and computer_choice == "kertas")
        ):
            print(f"Kamu Kalah!. Kamu memilih {user_choice} dan komputer memilih {computer_choice}")
            print("\t")

        elif user_choice in ["q", "quit"]:
            print("Anda keluar dari program.")
            break

        else:
            print("Pilihan yang anda masukan tidak valid!")
            print("\t")

if __name__ == "__main__":
    game()