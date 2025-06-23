from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):

        new_game = Game()

        grid = new_game.grid

        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
                assert letter in string.ascii_uppercase


    def test_empty_word_is_invalid(self):

        new_game = Game()
        assert new_game.is_valid('') is False

    def test_is_valid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'
        # exercise
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is True
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched

    def test_is_invalid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'
        # exercise
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is False
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched
