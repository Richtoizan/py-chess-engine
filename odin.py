import chess
import random

def evaluate(board):
    # Simple evaluation function: material difference
    return board.queens * 9 + board.rooks * 5 + board.bishops * 3 + board.knights * 3 + board.pawns

def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            board.pop()
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True)
            board.pop()
            min_eval = min(min_eval, eval)
        return min_eval

def player_move(board, move_str):
    try:
        move = chess.Move.from_uci(move_str)
        if move not in board.legal_moves:
            raise ValueError
    except ValueError:
        print("Invalid move. Please enter a valid move in UCI format (e.g., e2e4).")
        return None

    return move
def engine_move(board, search_depth=4):
    best_move = None
    best_eval = float('-inf')

    for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, search_depth - 1, False)
        board.pop()

        if eval > best_eval:
            best_move = move
            best_eval = eval

    if best_move is None:
        # If no move was found, choose a random legal move
        best_move = random.choice(list(board.legal_moves))

    return best_move

def main():
    board = chess.Board()

    while not board.is_game_over():
        print(board)

        # Player move
        move = None
        while move is None:
            move_str = input("Enter your move: ")
            move = player_move(board, move_str)

        board.push(move)

        # Check if game is over after player move
        if board.is_game_over():
            break

        # Engine move
        move = engine_move(board)
        board.push(move)

    print("Game over. Result:", board.result())

if __name__ == "__main__":
    main()