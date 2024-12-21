import random


def play_game():
    print("Willkommen zum Textbasierten Videospiel!")
    player_health = 100
    enemy_health = random.randint(50, 100)

    while player_health > 0 and enemy_health > 0:
        print("Dein aktuelles Leben: " + str(player_health))
        print("Gegnerische Leben: " + str(enemy_health))
        print("Wähle eine Aktion:")
        print("1. Angriff")
        print("2. Verteidigung")

        player_choice = input("Deine Wahl: ")

        if player_choice == "1":
            damage = random.randint(10, 20)
            enemy_health -= damage
            print("Du fügst dem Gegner " + str(damage) + " Schaden zu!")
        elif player_choice == "2":
            player_health += random.randint(5, 10)
            print("Du heilst dich für " + str(player_health) + " Leben!")

        enemy_damage = random.randint(5, 15)
        player_health -= enemy_damage
        print("Der Gegner fügt dir " + str(enemy_damage) + " Schaden zu!")

    if player_health <= 0:
        print("Game Over! Du hast verloren.")
    else:
        print("Gewonnen! Du hast den Gegner besiegt.")


play_game()