class user(FoodItem):
    
	def __init__(self, user_name):
	    self.user_name = user_name
		self.user_whishlist	= []
	    self.user_cart = []
		self.user_reviews = []

        def add_to_wishlist(self, food_item):    # Add a food item to the wishlist
			pass

    def add_to_cart(self, food_item):   # Add a food item to the cart
			pass

    def add_review(self, food_item, rating, comment):        # Add a review for a food item
			pass
		
	def view_profile(self):   # Display user profile (reviews, badges, etc.)
	        pass
