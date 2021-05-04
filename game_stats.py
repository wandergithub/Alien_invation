

class GameStats:
    """ Track statistics for Alien Invasion. """

    def __init__(self,ai_game):
        """ Initialice statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False
        # High score should never be reset.
        self.high_score = 0


    def reset_stats(self):
        """ Initialice statistics that can change during game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        