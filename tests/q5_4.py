test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert abs(average_20th_century_rating - 8.2783625730994146) < 1e-5
          >>> assert abs(average_21st_century_rating - 8.2379746835443033) < 1e-5
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
