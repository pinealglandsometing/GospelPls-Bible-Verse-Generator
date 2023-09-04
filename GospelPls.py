import random
import os
import time

# Define the list of Bible verses
bible_verses = [
    "For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life. - John 3:16",
    "Trust in the Lord with all your heart, and do not lean on your own understanding. - Proverbs 3:5",
    "I can do all things through him who strengthens me. - Philippians 4:13",
    "The Lord is my shepherd; I shall not want. - Psalm 23:1",
    "Be strong and courageous. Do not fear or be in dread of them, for it is the Lord your God who goes with you. - Deuteronomy 31:6",
     "For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life. - John 3:16",
    "Trust in the Lord with all your heart, and do not lean on your own understanding. - Proverbs 3:5",
    "I can do all things through him who strengthens me. - Philippians 4:13",
    "The Lord is my shepherd; I shall not want. - Psalm 23:1",
    "Be strong and courageous. Do not fear or be in dread of them, for it is the Lord your God who goes with you. - Deuteronomy 31:6",
    "In the beginning was the Word, and the Word was with God, and the Word was God. - John 1:1",
    "Jesus said to him, 'I am the way, and the truth, and the life. No one comes to the Father except through me.' - John 14:6",
    "Go therefore and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit. - Matthew 28:19",
    "For all have sinned and fall short of the glory of God. - Romans 3:23",
    "For by grace you have been saved through faith. And this is not your own doing; it is the gift of God. - Ephesians 2:8",
    "In the beginning, God created the heavens and the earth. - Genesis 1:1",
    "But you will receive power when the Holy Spirit has come upon you, and you will be my witnesses in Jerusalem and in all Judea and Samaria, and to the end of the earth. - Acts 1:8",
    "All Scripture is breathed out by God and profitable for teaching, for reproof, for correction, and for training in righteousness. - 2 Timothy 3:16",
    "If you confess with your mouth that Jesus is Lord and believe in your heart that God raised him from the dead, you will be saved. - Romans 10:9",
    "For the wages of sin is death, but the free gift of God is eternal life in Christ Jesus our Lord. - Romans 6:23",
    "Repent and be baptized every one of you in the name of Jesus Christ for the forgiveness of your sins, and you will receive the gift of the Holy Spirit. - Acts 2:38",
    "But to all who did receive him, who believed in his name, he gave the right to become children of God. - John 1:12",
    "And we know that for those who love God all things work together for good, for those who are called according to his purpose. - Romans 8:28",
    "The true light, which gives light to everyone, was coming into the world. - John 1:9",
    "Then God said, 'Let us make man in our image, after our likeness.' - Genesis 1:26",
    "I appeal to you therefore, brothers, by the mercies of God, to present your bodies as a living sacrifice, holy and acceptable to God, which is your spiritual worship. - Romans 12:1",
    "But God shows his love for us in that while we were still sinners, Christ died for us. - Romans 5:8",
    "And Jesus came and said to them, 'All authority in heaven and on earth has been given to me.' - Matthew 28:18",
    "Jesus answered him, 'Truly, truly, I say to you, unless one is born again he cannot see the kingdom of God.' - John 3:3",
    "And he said to them, 'Go into all the world and proclaim the gospel to the whole creation.' - Mark 16:15",
    "The thief comes only to steal and kill and destroy. I came that they may have life and have it abundantly. - John 10:10",
    "And the Word became flesh and dwelt among us, and we have seen his glory, glory as of the only Son from the Father, full of grace and truth. - John 1:14",
    "And there is salvation in no one else, for there is no other name under heaven given among men by which we must be saved. - Acts 4:12",
    "And they devoted themselves to the apostles' teaching and the fellowship, to the breaking of bread and the prayers. - Acts 2:42",
    "Now there was a man of the Pharisees named Nicodemus, a ruler of the Jews. - John 3:1",
    "But the fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faithfulness. - Galatians 5:22",
    "Trust in the LORD with all your heart, and do not lean on your own understanding. - Proverbs 3:5",
    "For I know the plans I have for you, declares the LORD, plans for welfare and not for evil, to give you a future and a hope. - Jeremiah 29:11",
    "On the third day there was a wedding at Cana in Galilee, and the mother of Jesus was there. - John 2:1",
    "he saved us, not because of works done by us in righteousness, but according to his own mercy, by the washing of regeneration and renewal of the Holy Spirit. - Titus 3:5",
    "Do not be conformed to this world, but be transformed by the renewal of your mind, that by testing you may discern what is the will of God, what is good and acceptable and perfect. - Romans 12:2",
    "Let not your hearts be troubled. Believe in God; believe also in me. - John 14:1",
    "Now when Jesus learned that the Pharisees had heard that Jesus was making and baptizing more disciples than John. - John 4:1",
    "And he gave the apostles, the prophets, the evangelists, the shepherds and teachers. - Ephesians 4:11",
    "Therefore, just as sin came into the world through one man, and death through sin, and so death spread to all men because all sinned. - Romans 5:12",
    "Come to me, all who labor and are heavy laden, and I will give you rest. - Matthew 11:28",
    "Therefore, since we have been justified by faith, we have peace with God through our Lord Jesus Christ. - Romans 5:1",
    "So God created man in his own image, in the image of God he created him; male and female he created them. - Genesis 1:27",
    "For I am not ashamed of the gospel, for it is the power of God for salvation to everyone who believes, to the Jew first and also to the Greek. - Romans 1:16",
    "If we confess our sins, he is faithful and just to forgive us our sins and to cleanse us from all unrighteousness. - 1 John 1:9",
    "When the day of Pentecost arrived, they were all together in one place. - Acts 2:1",
    "Therefore, if anyone is in Christ, he is a new creation. The old has passed away; behold, the new has come. - 2 Corinthians 5:17",
    "Now faith is the assurance of things hoped for, the conviction of things not seen. - Hebrews 11:1",
    "Do your best to present yourself to God as one approved, a worker who has no need to be ashamed, rightly handling the word of truth. - 2 Timothy 2:15",
    "There is therefore now no condemnation for those who are in Christ Jesus. - Romans 8:1",
    "For 'everyone who calls on the name of the Lord will be saved.' - Romans 10:13",
    "And you will know the truth, and the truth will set you free. - John 8:32",
    "For to us a child is born, to us a son is given; and the government shall be upon his shoulder, and his name shall be called Wonderful Counselor, Mighty God, Everlasting Father, Prince of Peace. - Isaiah 9:6",
    "If you love me, you will keep my commandments. - John 14:15",
    "Hear, O Israel: The LORD our God, the LORD is one. - Deuteronomy 6:4",
    "A new commandment I give to you, that you love one another: just as I have loved you, you also are to love one another. - John 13:34",
    "God is spirit, and those who worship him must worship in spirit and truth. - John 4:24",
    "I can do all things through him who strengthens me. - Philippians 4:13",
    "And you were dead in the trespasses and sins. - Ephesians 2:1",
    "And I will ask the Father, and he will give you another Helper, to be with you forever. - John 14:16",
    "The earth was without form and void, and darkness was over the face of the deep. And the Spirit of God was hovering over the face of the waters. - Genesis 1:2",
    "For the word of God is living and active, sharper than any two-edged sword, piercing to the division of soul and of spirit, of joints and of marrow, and discerning the thoughts and intentions of the heart. - Hebrews 4:12",
    "Therefore, confess your sins to one another and pray for one another, that you may be healed. The prayer of a righteous person has great power as it is working. - James 5:16",
    "Therefore the Lord himself will give you a sign. Behold, the virgin shall conceive and bear a son, and shall call his name Immanuel. - Isaiah 7:14",
    "But if we walk in the light, as he is in the light, we have fellowship with one another, and the blood of Jesus his Son cleanses us from all sin. - 1 John 1:7",
    "Jesus answered, 'Truly, truly, I say to you, unless one is born of water and the Spirit, he cannot enter the kingdom of God.' - John 3:5",
    "Have this mind among yourselves, which is yours in Christ Jesus. - Philippians 2:5",
    "The next day he saw Jesus coming toward him, and said, 'Behold, the Lamb of God, who takes away the sin of the world!' - John 1:29",
    "For the wrath of God is revealed from heaven against all ungodliness and unrighteousness of men, who by their unrighteousness suppress the truth. - Romans 1:18",
    "Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God. - Philippians 4:6",
    "Therefore, since we are surrounded by so great a cloud of witnesses, let us also lay aside every weight, and sin which clings so closely, and let us run with endurance the race that is set before us. - Hebrews 12:1",
    "All things were made through him, and without him was not any thing made that was made. - John 1:3",
    "And I tell you, you are Peter, and on this rock I will build my church, and the gates of hell shall not prevail against it. - Matthew 16:18",
    "Now these Jews were more noble than those in Thessalonica; they received the word with all eagerness, examining the Scriptures daily to see if these things were so. - Acts 17:11",
    "I have been crucified with Christ. It is no longer I who live, but Christ who lives in me. And the life I now live in the flesh I live by faith in the Son of God, who loved me and gave himself for me. - Galatians 2:20",
    "When the Son of Man comes in his glory, and all the angels with him, then he will sit on his glorious throne. - Matthew 25:31",
    "Do not think that I have come to abolish the Law or the Prophets; I have not come to abolish them but to fulfill them. - Matthew 5:17",
    "So faith comes from hearing, and hearing through the word of Christ. - Romans 10:17",
    "But seek first the kingdom of God and his righteousness, and all these things will be added to you. - Matthew 6:33",
    "The Spirit of the Lord is upon me, because he has anointed me to proclaim good news to the poor. He has sent me to proclaim liberty to the captives and recovering of sight to the blind, to set at liberty those who are oppressed. - Luke 4:18",
    "When the Spirit of truth comes, he will guide you into all the truth, for he will not speak on his own authority, but whatever he hears he will speak, and he will declare to you the things that are to come. - John 16:13",
    "Pay careful attention to yourselves and to all the flock, in which the Holy Spirit has made you overseers, to care for the church of God, which he obtained with his own blood. - Acts 20:28",
    "For the grace of God has appeared, bringing salvation for all people. - Titus 2:11",
    "You are of your father the devil, and your will is to do your father's desires. He was a murderer from the beginning, and does not stand in the truth, because there is no truth in him. When he lies, he speaks out of his own character, for he is a liar and the father of lies. - John 8:44",
    "Finally, be strong in the Lord and in the strength of his might. - Ephesians 6:10",
    "Let every person be subject to the governing authorities. For there is no authority except from God, and those that exist have been instituted by God. - Romans 13:1",
    "And making a whip of cords, he drove them all out of the temple, with the sheep and oxen. And he poured out the coins of the money-changers and overturned their tables. - John 2:15",
    "Whoever believes and is baptized will be saved, but whoever does not believe will be condemned. - Mark 16:16",
    "As it is written: 'None is righteous, no, not one.' - Romans 3:10",
    "I will put enmity between you and the woman, and between your offspring and her offspring; he shall bruise your head, and you shall bruise his heel. - Genesis 3:15",
    "And without faith it is impossible to please him, for whoever would draw near to God must believe that he exists and that he rewards those who seek him. - Hebrews 11:6",
    "But the Helper, the Holy Spirit, whom the Father will send in my name, he will teach you all things and bring to your remembrance all that I have said to you. - John 14:26",
    "Truly, truly, I say to you, whoever hears my word and believes him who sent me has eternal life. He does not come into judgment, but has passed from death to life. - John 5:24",
    "And it shall come to pass afterward, that I will pour out my Spirit on all flesh; your sons and your daughters shall prophesy, your old men shall dream dreams, and your young men shall see visions. - Joel 2:28",
    "And God said, 'Let the earth sprout vegetation, plants yielding seed, and fruit trees bearing fruit in which is their seed, each according to its kind, on the earth.' And it was so. - Genesis 1:11",
    "Count it all joy, my brothers, when you meet trials of various kinds. - James 1:2",
    "He is the image of the invisible God, the firstborn of all creation. - Colossians 1:15",
    "And he said to him, 'You shall love the Lord your God with all your heart and with all your soul and with all your mind. - Matthew 22:37",
    "waiting for our blessed hope, the appearing of the glory of our great God and Savior Jesus Christ. - Titus 2:13",
    "Finally, brothers, whatever is true, whatever is honorable, whatever is just, whatever is pure, whatever is lovely, whatever is commendable, if there is any excellence, if there is anything worthy of praise, think about these things. - Philippians 4:8",
    "And when he had said these things, as they were looking on, he was lifted up, and a cloud took him out of their sight. - Acts 1:9",
    "Beloved, let us love one another, for love is from God, and whoever loves has been born of God and knows God. - 1 John 4:7",
    "He has told you, O man, what is good; and what does the LORD require of you but to do justice, and to love kindness, and to walk humbly with your God? - Micah 6:8",
    "Sanctify them in the truth; your word is truth. - John 17:17",
    "You shall not lie with a male as with a woman; it is an abomination. - Leviticus 18:22",
    "On the first day of the week, when we were gathered together to break bread, Paul talked with them, intending to depart on the next day, and he prolonged his speech until midnight. - Acts 20:7",
    "And they said, 'Believe in the Lord Jesus, and you will be saved, you and your household.' - Acts 16:31",
    "Jesus said to her, 'I am the resurrection and the life. Whoever believes in me, though he die, yet shall he live.' - John 11:25",
    "Jesus said to them, 'Truly, truly, I say to you, before Abraham was, I am.' - John 8:58",
    "And they were all filled with the Holy Spirit and began to speak in other tongues as the Spirit gave them utterance. - Acts 2:4",
    "I am the vine; you are the branches. Whoever abides in me and I in him, he it is that bears much fruit, for apart from me you can do nothing. - John 15:5",
    "So those who received his word were baptized, and there were added that day about three thousand souls. - Acts 2:41",
    "Train up a child in the way he should go; even when he is old he will not depart from it. - Proverbs 22:6",
    "Now the serpent was more crafty than any other beast of the field that the LORD God had made. He said to the woman, 'Did God actually say, 'You shall not eat of any tree in the garden'?' - Genesis 3:1",
    "If any of you lacks wisdom, let him ask God, who gives generously to all without reproach, and it will be given him. - James 1:5",
    "Long ago, at many times and in many ways, God spoke to our fathers by the prophets. - Hebrews 1:1",
    "For the sake of the truth that abides in us and will be with us forever: - 2 John 1:2",
    "And this is eternal life, that they know you, the only true God, and Jesus Christ whom you have sent. - John 17:3",
    "There was a rich man who was clothed in purple and fine linen and who feasted sumptuously every day. - Luke 16:19",
    "For there are three that testify: the Spirit and the water and the blood; and these three agree. - 1 John 5:7",
    "So Jesus said to the Jews who had believed him, 'If you abide in my word, you are truly my disciples.' - John 8:31",
    "that you may have certainty concerning the things you have been taught. - Luke 1:4",
    "Behold, I stand at the door and knock. If anyone hears my voice and opens the door, I will come in to him and eat with him, and he with me. - Revelation 3:20",
    "if indeed you have tasted that the Lord is good. - 1 Peter 2:3",
    "I and the Father are one. - John 10:30",
    "but in your hearts honor Christ the Lord as holy, always being prepared to make a defense to anyone who asks you for a reason for the hope that is in you; yet do it with gentleness and respect. - 1 Peter 3:15",
    "Not everyone who says to me, 'Lord, Lord,' will enter the kingdom of heaven, but the one who does the will of my Father who is in heaven. - Matthew 7:21",
    "Whoever believes in him is not condemned, but whoever does not believe is condemned already, because he has not believed in the name of the only Son of God. - John 3:18",
    "Now the LORD said to Abram, 'Go from your country and your kindred and your father's house to the land that I will show you. - Genesis 12:1"
    # Add more Bible verses here
]

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to generate a random Bible verse
def generate_bible_verse():
    clear_screen()
    verse = random.choice(bible_verses)
    print("Welcome to GospelPls Bible Verse Generator V1")
    print("--------------------")
    print("Please type '1' to generate a Bible Verse!")
    print("Please type '2' to go back to the Main Menu")
    print("--------------------")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print(verse)
        input("Press Enter to continue...")
        return False  # Continue in the GospelPls menu
    elif choice == "2":
        clear_screen()
        return True  # Go back to the Main Menu
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
        return False  # Continue in the GospelPls menu

# Function for the GospelPls menu
def gospel_pls_menu():
    while True:
        clear_screen()
        go_back = generate_bible_verse()
        if go_back:
            return

# Function to display The Lord's Prayer
def display_lords_prayer():
    clear_screen()
    print("The Lord’s Prayer – Matthew 6:9-13")
    print("----------------------------------")
    print("Our Father, who art in heaven,\n"
          "hallowed be thy Name,\n"
          "thy Kingdom come,\n"
          "thy will be done,\n"
          "on earth as it is in heaven.\n"
          "Give us this day our daily bread.\n"
          "And forgive us our trespasses,\n"
          "as we forgive those\n"
          "who trespass against us.\n"
          "And lead us not into temptation,\n"
          "but deliver us from evil.\n"
          "For thine is the kingdom,\n"
          "the power, and the glory,\n"
          "for ever and ever. Amen.")
    input("Press Enter to continue...")
    clear_screen()

# Function to display the Twenty-Third Psalm
def display_twenty_third_psalm():
    clear_screen()
    print("Twenty-Third Psalm – Psalms 23: 1-6")
    print("------------------------------------")
    print("The Lord is my shepherd; I shall not want.\n"
          "He maketh me to lie down in green pastures:\n"
          "he leadeth me beside the still waters.\n"
          "He restoreth my soul: he leadeth me in the\n"
          "paths of righteousness for his name's sake.\n"
          "Yea, though I walk through the valley of the\n"
          "shadow of death, I will fear no evil: for thou\n"
          "art with me; thy rod and thy staff they comfort me.\n"
          "Thou preparest a table before me in the presence\n"
          "of mine enemies: thou anointest my head with oil;\n"
          "my cup runneth over.\n"
          "Surely goodness and mercy shall follow me all the\n"
          "days of my life: and I will dwell in the house of\n"
          "the Lord for ever.")
    input("Press Enter to continue...")
    clear_screen()

# Function to display The Serenity Prayer
def display_serenity_prayer():
    clear_screen()
    print("The Serenity Prayer – Reinhold Niebuhr")
    print("--------------------------------------")
    print("God, grant me the serenity to accept the things\n"
          "I cannot change,\n"
          "Courage to change the things I can,\n"
          "And wisdom to know the difference.")
    input("Press Enter to continue...")
    clear_screen()

# Function to display the Instrument of Your Peace
def display_instrument_of_your_peace():
    clear_screen()
    print("Instrument of Your Peace – St. Francis of Assisi")
    print("-------------------------------------------------")
    print("Lord, make me an instrument of your peace.\n"
          "Where there is hatred, let me sow love;\n"
          "where there is injury, pardon;\n"
          "where there is doubt, faith;\n"
          "where there is despair, hope;\n"
          "where there is darkness, light;\n"
          "where there is sadness, joy.\n"
          "Grant that I may not so much seek\n"
          "to be consoled as to console;\n"
          "to be understood as to understand;\n"
          "to be loved as to love.\n"
          "For it is in giving that we receive;\n"
          "it is in pardoning that we are pardoned;\n"
          "and it is in dying that we are born to eternal life.")
    input("Press Enter to continue...")
    clear_screen()

# Function to display the Hail Mary
def display_hail_mary():
    clear_screen()
    print("Hail Mary")
    print("---------")
    print("Hail Mary, full of grace,\n"
          "the Lord is with thee;\n"
          "blessed art thou among women,\n"
          "and blessed is the fruit of thy womb, Jesus.\n"
          "Holy Mary, Mother of God,\n"
          "pray for us sinners,\n"
          "now and at the hour of our death.\n"
          "Amen.")
    input("Press Enter to continue...")
    clear_screen()

# Function for the Prayers menu
def prayers_menu():
    while True:
        clear_screen()
        print("Welcome to GospelPls' Top 5 Favourite Prayers")
        print("------------------------------")
        print("1. The Lord’s Prayer – Matthew 6:9-13")
        print("2. Twenty-Third Psalm – Psalms 23: 1-6")
        print("3. The Serenity Prayer – Reinhold Niebuhr")
        print("4. Instrument of Your Peace – St. Francis of Assisi")
        print("5. Hail Mary")
        print("--------------------")
        choice = input("Enter your choice (1-5 or back): ")
        if choice == "1":
            display_lords_prayer()
        elif choice == "2":
            display_twenty_third_psalm()
        elif choice == "3":
            display_serenity_prayer()
        elif choice == "4":
            display_instrument_of_your_peace()
        elif choice == "5":
            display_hail_mary()
        elif choice.lower() == "back":
            clear_screen()
            return
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

# Display the welcome message
print("Welcome to the GospelPls Bible Verse Generator!")
print("--------------------------------------------")

# Loop to continuously listen for user input
while True:
    # Display the main menu
    clear_screen()
    print("The GospelPls Generator Main Menu:")
    print("--------------------------------------------")
    print("1. GospelPls")
    print("2. Prayers")
    print("3. Exit")
    print("--------------------")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        gospel_pls_menu()
    elif choice == "2":
        prayers_menu()
    elif choice == "3":
        clear_screen()
        print("Thank you for using the GospelPls Bible Verse Generator. Goodbye!")
        time.sleep(2)  # Delay for 2 seconds before exiting
        clear_screen()
        break
    else:
        print("Invalid choice. Please try again.")
        print("--------------------")
        input("Press Enter to continue...")
