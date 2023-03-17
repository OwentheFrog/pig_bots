def choice(round_score, my_score, opponent_score):
    if my_score - opponent_score > 20:
              if score >= 25:
                  return False
              else:
                  return True
          elif my_score - opponent_score > 10:
              if score >= 18:
                  return False
              else:
                  return True
          elif my_score > opponent_score:
              if score >= 15:
                  return False
              else:
                  return True
          elif my_score + 20 > opponent_score:
              if score >= 15:
                  return False
              else:
                  return True
          elif my_score == opponent_score:
              if score >= 15:
                  return False
              else:
                  return True
          else:
              return False
