

import time


class Olympics(object):
	
    countries = []
	
    def __init__(self, name):
	    self.name = name + " 2016"
	
    def add_country(self, country):
		self.country = country  
		self.countries.append(self.country)


class Country(object):
	
	gold = 0
	silver = 0
	bronze = 0
	ath_dir = []
	
	def __init__(self, name, athletes):
		self.name = name
		self.athletes = athletes
	
	def add_medal(self, color):
	    self.color = color
	    
	    if color.lower() == "gold": self.gold += 1
	    elif color.lower() == "silver": self.silver += 1
	    elif color.lower() == "bronze": self.bronze += 1
	    else: print "Invalid medal"
	
	def get_medal(self, color):
	    self.color2 = color
	    
	    if self.color2 == "gold": return self.gold
	    elif self.color2 == "silver": return self.silver
	    elif self.color2 == "bronze": return self.bronze
	    else: print "Invalid medal"
	
	def add_ath(self, athlete):
	    self.ath = athlete
	    self.ath_dir.append(self.ath)

class Athlete(object):
	
	def __init__(self, name, age, sport):
		self.name = name
		self.age = age
		self.sport = sport

		
class Event(object):
	
	event = ""
	
	def __init__(self, name):
		self.name = name
		self.event = name
	
	def commence(self):
	    
	    if self.event == "Type to 3":
	        print "The game is 'Type to 3'. You have three tries to count to the number three."
	        time.sleep(1)
	        one = int(raw_input("> "))
	        if one == 1: 
	            two = int(raw_input("> "))
	            
	            if two == 2: 
	                three = int(raw_input("> "))
	                
	                if three == 3:  
	                    print "You win!"
	                else: 
	                    print "Lost"
	                    
	            else: 
	                print "Lost"
	                
	        else: 
	            print "Lost"
	       
	        print "Game over"
	       
	        
	


class Engine(object):
    
    def __init__(self, games):
        self.games = games
    
    def play(self):
        
        country1 = Country("USA", 3)
        
        games.add_country(country1)
        
        print games.countries[0].name, games.countries[0].athletes
        
        #games.countries[0].add_medal("gold")
        #games.countries[0].add_medal("gold")
        #games.countries[0].add_medal("platinum")
        
        #print games.countries[0].get_medal("gold")
        
        phelps = Athlete("Phelps", 31, "Swimming")
        games.countries[0].add_ath(phelps)
        print games.countries[0].ath_dir[0].name
        
        event1 = Event("Type to 3")
        event1.commence()


# Testing #

games = Olympics("North Falmouth")
play = Engine(games)
play.play()

























    